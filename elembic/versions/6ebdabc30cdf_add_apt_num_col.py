"""add apt num col

Revision ID: 6ebdabc30cdf
Revises: 5281925afe8e
Create Date: 2022-10-30 15:50:33.769069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ebdabc30cdf'
down_revision = '5281925afe8e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('address', 'apt_num')
