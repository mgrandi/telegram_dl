from __future__ import annotations

import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
import telegram_dl.db_model_enums as dbme
from telegram_dl import constants
from telegram_dl import utils

logger = logging.getLogger(__name__)

class TextEntityAide:

    @staticmethod
    def get_text_entity_from_tdlib_text_entity(
        db_model_message_ver:db_model.MessageVersion,
        tdlib_text_entity:db_model.TextEntity
        ) -> db_model.TextEntity:
        '''
        creates a db_model.TextEntity using the data from the passed in
        `tdlib_generated.textEntity` and a `db_model.MessageVersion`

        '''

        new_entity = db_model.TextEntity(
            message_version_text=db_model_message_ver,
            offset=tdlib_text_entity.offset,
            length=tdlib_text_entity.length,
            text_entity_type=dbme.TextEntityTypeEnum.parse_from_tdg_text_entity_type(tdlib_text_entity.type))

        return new_entity

    @staticmethod
    def get_text_entities_from_tdlib_text_entity_sequence(
        db_model_message_ver:db_model.MessageVersion,
        tdlib_text_entities_sequence:typing.Sequence[tdg.textEntity]
        ) -> typing.Sequence[db_model.TextEntity]:
        '''
        given a sequence of `tdlib_generated.textEntity` objects, create a
        sequence of `db_model.TextEntity` objects using the data from each one
        and a `db_model.MessageVersion`

        '''

        result_list = []

        for iter_tdlib_te in tdlib_text_entities_sequence:

            db_model_te = TextEntityAide.get_text_entity_from_tdlib_text_entity(
                db_model_message_ver, iter_tdlib_te)

            result_list.append(db_model_te)

        return result_list


    @staticmethod
    def compare_dbmodel_and_tdlib_text_entities(
        dbmodel_text_entities:typing.Sequence[db_model.TextEntity],
        tdlib_message:tdg.message) -> bool:
        '''
        method that compares a sequence of `db_model.TextEntity` objects
        with a sequence of `tdlib_generated.textEntity` objects

        '''

        logger.debug("comparing: `%s` and `%s`", dbmodel_text_entities, tdlib_message)


        # here go through and check all of the `tdg.textEntity` that are
        # in the `messageText.text.entities` list and then compare them
        # in a loop to the `TextEntity` objects that the
        # given `MessageVersionText` has

        # do fast comparison, if the number of entities differ then we know we have
        # a difference

        if not isinstance(tdlib_message.content, tdg.messageText):
            logger.error(
                utils.strip_margin('''compare_dbmodel_and_tdlib_text_entities somehow got a tdg.message
                    |that didn't have a messageText content type! tdlib_message: `%s`, dbmodel_text_entities: `%s`'''),
                tdlib_message, dbmodel_text_entities
            )

        tdlib_message_text_entities_list = tdlib_message.content.text.entities

        tdl_len = len(dbmodel_text_entities)
        tdg_len = len(tdlib_message_text_entities_list)

        if tdl_len != tdg_len:
            logger.debug(utils.strip_margin('''fast comparison,
                |returning False because the lengths are different tdl: `%s` and
                |tdg: `%s`'''), tdl_len, tdg_len)

            return False

        # make a copy of the list so we don't accidentally remove them from the database
        # when we remove from this list to make the searching slightly faster
        tdl_text_entities_list_copy = [x for x in dbmodel_text_entities]

        for iter_tdg_text_entity in tdlib_message_text_entities_list:

            found = None
            for iter_tdl_text_entity in tdl_text_entities_list_copy:

                tdg_te_type = dbme.TextEntityTypeEnum.parse_from_tdg_text_entity_type(iter_tdg_text_entity.type)
                tmp_result = \
                    iter_tdl_text_entity.message_version_text.message.tg_message_id == tdlib_message.id \
                    and iter_tdl_text_entity.offset == iter_tdg_text_entity.offset \
                    and iter_tdl_text_entity.length == iter_tdg_text_entity.length \
                    and iter_tdl_text_entity.text_entity_type == tdg_te_type

                if tmp_result:
                    # found a match, set it to `found` and break so we can remove it
                    found = iter_tdl_text_entity
                    break

            # if we found a match, remove it, if we didn't, then we can return false immediately
            if found:
                tdl_text_entities_list_copy.remove(found)
                found = None
                continue
            else:
                logger.debug(utils.strip_margin('''returning false, found text entity in tdg message
                    |that doesn't exist in tdl message: `%s`'''), iter_tdg_text_entity)
                return False

        # if we get here we have found all of the text entities and they all match, return true
        logger.debug("all text entities match, returning true")

        return True



