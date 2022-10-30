"""create address_id to users

Revision ID: 5281925afe8e
Revises: 8c170d63e929
Create Date: 2022-10-30 13:31:36.035679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5281925afe8e'
down_revision = '8c170d63e929'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True)),
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=["id"],ondelete="CASCADE")


def downgrade() :
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column("users", "address_id")
