"""empty message

Revision ID: 95e813ec478c
Revises: 
Create Date: 2017-04-17 11:33:07.367274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95e813ec478c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cunt', sa.Column('votes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cunt', 'votes')
    # ### end Alembic commands ###
