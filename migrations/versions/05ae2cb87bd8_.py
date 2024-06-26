"""empty message

Revision ID: 05ae2cb87bd8
Revises: 96515b407714
Create Date: 2024-04-17 11:36:12.150668

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '05ae2cb87bd8'
down_revision = '96515b407714'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.alter_column('model',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=60),
               existing_nullable=False)
        batch_op.drop_index('model')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.create_index('model', ['model'], unique=True)
        batch_op.alter_column('model',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###
