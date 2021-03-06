"""empty message

Revision ID: f91774764154
Revises: 760d2933d1ed
Create Date: 2021-07-11 16:52:21.226504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f91774764154'
down_revision = '760d2933d1ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting', sa.Column('number_of_attendants', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meeting', 'number_of_attendants')
    # ### end Alembic commands ###
