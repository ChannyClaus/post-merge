"""empty message

Revision ID: c469bb322b5d
Revises: d889cac0d4f1
Create Date: 2024-10-09 23:21:43.549186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c469bb322b5d'
down_revision: Union[str, None] = 'd889cac0d4f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
