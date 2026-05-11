"""add foreign-key to posts table 

Revision ID: 5441c4db5945
Revises: d80e9940bf10
Create Date: 2026-05-11 11:56:57.388130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5441c4db5945'
down_revision = 'd80e9940bf10'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
