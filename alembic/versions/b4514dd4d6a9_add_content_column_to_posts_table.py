"""add content column to posts table 

Revision ID: b4514dd4d6a9
Revises: 23786518cb77
Create Date: 2026-05-11 11:39:52.086999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4514dd4d6a9'
down_revision = '23786518cb77'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
