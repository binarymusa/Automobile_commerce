"""empty message

Revision ID: 96515b407714
Revises: ecbef2677a0b
Create Date: 2024-04-16 12:45:51.873112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96515b407714'
down_revision = 'ecbef2677a0b'
branch_labels = None
depends_on = None


def upgrade():
   # Adding car_type column
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('car_type', sa.String(length=30), nullable=True))


def downgrade():
    # Dropping car_type column
    with op.batch_alter_table('vehicles', schema=None) as batch_op:
        batch_op.drop_column('car_type')