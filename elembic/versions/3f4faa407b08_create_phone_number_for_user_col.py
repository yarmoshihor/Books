"""create phone number for user col

Revision ID: 3f4faa407b08
Revises: 
Create Date: 2022-10-29 20:16:36.419351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f4faa407b08'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
