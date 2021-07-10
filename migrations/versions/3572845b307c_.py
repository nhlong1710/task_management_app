"""empty message

Revision ID: 3572845b307c
Revises: dfc166a75b37
Create Date: 2021-07-09 18:46:32.898791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3572845b307c'
down_revision = 'dfc166a75b37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting', sa.Column('created_time', sa.DateTime(), nullable=True))
    op.add_column('meeting', sa.Column('meeting_end', sa.Float(), nullable=True))
    op.add_column('meeting', sa.Column('meeting_start', sa.Float(), nullable=True))
    op.add_column('meeting', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.add_column('meeting_user', sa.Column('response_date', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('expired_date', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('created_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_time')
    op.drop_column('task', 'expired_date')
    op.drop_column('meeting_user', 'response_date')
    op.drop_column('meeting', 'update_time')
    op.drop_column('meeting', 'meeting_start')
    op.drop_column('meeting', 'meeting_end')
    op.drop_column('meeting', 'created_time')
    # ### end Alembic commands ###
