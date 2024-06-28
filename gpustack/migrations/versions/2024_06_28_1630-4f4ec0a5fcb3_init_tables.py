"""init tables

Revision ID: 4f4ec0a5fcb3
Revises: 
Create Date: 2024-06-28 16:30:35.094815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import gpustack


# revision identifiers, used by Alembic.
revision: str = '4f4ec0a5fcb3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('system_loads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.Integer(), nullable=False),
    sa.Column('cpu', gpustack.schemas.common.JSON(), nullable=True),
    sa.Column('memory', gpustack.schemas.common.JSON(), nullable=True),
    sa.Column('gpu', gpustack.schemas.common.JSON(), nullable=True),
    sa.Column('gpu_memory', gpustack.schemas.common.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('full_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('require_password_change', sa.Boolean(), nullable=False),
    sa.Column('foo', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workers',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hostname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ip', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('labels', sa.JSON(), nullable=True),
    sa.Column('state', sa.Enum('unknown', 'running', 'inactive', name='workerstateenum'), nullable=False),
    sa.Column('status', gpustack.schemas.common.JSON(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workers_name'), 'workers', ['name'], unique=True)
    op.create_table('model_instances',
    sa.Column('source', sa.Enum('HUGGING_FACE', 'OLLAMA_LIBRARY', name='sourceenum'), nullable=False),
    sa.Column('huggingface_repo_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('huggingface_filename', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('ollama_library_model_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.Column('worker_ip', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('download_progress', sa.Float(), nullable=True),
    sa.Column('state', sa.Enum('initializing', 'pending', 'running', 'scheduled', 'error', 'downloading', name='modelinstancestateenum'), nullable=False),
    sa.Column('state_message', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('computed_resource_claim', gpustack.schemas.common.JSON(), nullable=True),
    sa.Column('gpu_index', sa.Integer(), nullable=True),
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('model_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['model_id'], ['models.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model_usages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('prompt_token_count', sa.Integer(), nullable=False),
    sa.Column('completion_token_count', sa.Integer(), nullable=False),
    sa.Column('request_count', sa.Integer(), nullable=False),
    sa.Column('operation', sa.Enum('CHAT_COMPLETION', name='operationenum'), nullable=False),
    sa.ForeignKeyConstraint(['model_id'], ['models.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model_usages')
    op.drop_table('model_instances')
    op.drop_index(op.f('ix_workers_name'), table_name='workers')
    op.drop_table('workers')
    op.drop_table('users')
    op.drop_table('system_loads')
    # ### end Alembic commands ###
