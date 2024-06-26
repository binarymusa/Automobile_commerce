"""empty message

Revision ID: b1552242f6fe
Revises: f5c6733158c7
Create Date: 2024-04-13 15:27:58.259046

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b1552242f6fe'
down_revision = 'f5c6733158c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_column('name2')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name2', mysql.VARCHAR(length=1023), nullable=True))

    # ### end Alembic commands ###
