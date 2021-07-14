"""empty message

Revision ID: d82e13368947
Revises: 98995bc7df2f
Create Date: 2021-07-11 10:11:34.818056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd82e13368947'
down_revision = '98995bc7df2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting', sa.Column('meeting_description', sa.String(), nullable=True))
    op.drop_column('meeting', 'meeting_desription')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting', sa.Column('meeting_desription', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('meeting', 'meeting_description')
    # ### end Alembic commands ###