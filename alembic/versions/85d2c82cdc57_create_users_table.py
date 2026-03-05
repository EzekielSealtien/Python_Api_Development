"""create_users_table

Revision ID: 85d2c82cdc57
Revises: 5eaf87fae99b
Create Date: 2026-03-05 11:28:54.737507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85d2c82cdc57'
down_revision: Union[str, Sequence[str], None] = '5eaf87fae99b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )  
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
