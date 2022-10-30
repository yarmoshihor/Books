"""Create address table

Revision ID: 8c170d63e929
Revises: d9b5cb74f31f
Create Date: 2022-10-30 13:03:16.283965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c170d63e929'
down_revision = 'd9b5cb74f31f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String, nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column("postalcode", sa.String(), nullable=False)
                    )


def downgrade():
    op.drop_table('address')
