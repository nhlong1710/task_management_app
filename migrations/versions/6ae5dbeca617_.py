"""empty message

Revision ID: 6ae5dbeca617
Revises: f91774764154
Create Date: 2021-07-11 18:37:43.577469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ae5dbeca617'
down_revision = 'f91774764154'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting', sa.Column('number_of_responses', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meeting', 'number_of_responses')
    # ### end Alembic commands ###