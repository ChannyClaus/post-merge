"""empty message

Revision ID: 7ba77cf07c0b
Revises: dc4c065ed7e1
Create Date: 2024-10-08 00:44:29.556258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ba77cf07c0b'
down_revision: Union[str, None] = 'dc4c065ed7e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
