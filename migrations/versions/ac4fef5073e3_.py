"""empty message

Revision ID: ac4fef5073e3
Revises: 3572845b307c
Create Date: 2021-07-10 12:15:04.297511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac4fef5073e3'
down_revision = '3572845b307c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('update_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'update_time')
    # ### end Alembic commands ###
