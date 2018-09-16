"""initsss

Revision ID: 045b6e97dc50
Revises: bd890b3f629e
Create Date: 2018-09-15 22:07:55.465112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '045b6e97dc50'
down_revision = 'bd890b3f629e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('name', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'name')
    # ### end Alembic commands ###