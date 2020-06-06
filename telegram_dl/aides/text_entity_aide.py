from __future__ import annotations

import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
import telegram_dl.db_model_enums as dbme
from telegram_dl import constants

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




