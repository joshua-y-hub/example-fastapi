"""add user table

Revision ID: d80e9940bf10
Revises: b4514dd4d6a9
Create Date: 2026-05-11 11:46:10.436552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd80e9940bf10'
down_revision = 'b4514dd4d6a9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                     sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
                     sa.Column('email', sa.String(), nullable=False),
                     sa.Column('password', sa.String(), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email'))
    pass

def downgrade():
    op.drop_table('users')
    pass
