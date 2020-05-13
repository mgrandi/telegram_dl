# Code Snippets

just some code snippets that I reference often and would like to copy/paste

## SQLAlchemy model class

(sublime text doesn't like the python3 code snippet identifier?)

```python

class SomeModelClass(CustomDeclarativeBase):
    __tablename__ = 'some_model_class'

    # our unique identifier, primary key column
    some_model_class_id = Column(Intege, nullable=False)

    something = Column(Unicode, nullable=True)

    something_two = Column(Integer,
        ForeignKey("something_else.something_two"
            name="FK-some_model_class-something_two-something_else-something_two"))

    #############################
    # SQLAlchemy Relationships
    #############################

    something_three = relationship("SomethingElse")

    #############################
    # Table and Mapper Arguments
    #############################

    __mapper_args__ = {

    }

    __table_args__ = (
        PrimaryKeyConstraint("some_model_class_id",
            name="PK-some_model_class-some_model_class_id"),
        Index("IXUQ-some_model_class-something", "something", unique=True)
    )

```