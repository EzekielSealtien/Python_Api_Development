"""create_table_posts

Revision ID: 5eaf87fae99b
Revises: 
Create Date: 2026-03-05 11:12:54.726484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5eaf87fae99b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('now()'), nullable=False)) 
    pass

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')  # pylint: disable=no-member
    pass
