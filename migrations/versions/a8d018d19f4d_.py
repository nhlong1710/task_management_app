"""empty message

Revision ID: a8d018d19f4d
Revises: 6ae5dbeca617
Create Date: 2021-07-14 16:33:23.529372

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a8d018d19f4d'
down_revision = '6ae5dbeca617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meeting', 'meeting_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meeting', sa.Column('meeting_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###