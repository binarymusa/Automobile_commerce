"""empty message

Revision ID: 85b05f7bc970
Revises: 5a5273e40075
Create Date: 2024-08-06 19:39:06.001666

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '85b05f7bc970'
down_revision = '5a5273e40075'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('importations', schema=None) as batch_op:
        batch_op.alter_column('chasis_No',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=60),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('importations', schema=None) as batch_op:
        batch_op.alter_column('chasis_No',
               existing_type=sa.String(length=60),
               type_=mysql.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###