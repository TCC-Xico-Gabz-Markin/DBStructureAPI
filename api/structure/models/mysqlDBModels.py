from pydantic import BaseModel, Field
from api.common.helpers.objectid import PydanticObjectId
from api.structure.models.tableModels import TableModel


class DatabaseModel(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    name: str
    tables: list[TableModel]


class UpdateDBTablesQuery(BaseModel):
    db_id: PydanticObjectId
    db_name: str


class InterfaceQueryRequest(BaseModel):
    db_id: PydanticObjectId
    db_name: str
    order: str
