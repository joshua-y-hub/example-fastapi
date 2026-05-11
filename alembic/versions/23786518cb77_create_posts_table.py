"""create posts table

Revision ID: 23786518cb77
Revises: 
Create Date: 2026-05-08 18:01:53.856354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23786518cb77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), primary_key=True,nullable=False),sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
