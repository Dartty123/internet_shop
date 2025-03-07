"""Initial migration.

Revision ID: 42634642d874
Revises: 
Create Date: 2025-02-08 11:08:40.105780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42634642d874'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('_password')

    # ### end Alembic commands ###
