"""empty message

Revision ID: ea949c1f8747
Revises: e14bc49bed87
Create Date: 2024-10-10 01:45:22.671050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea949c1f8747'
down_revision: Union[str, None] = 'e14bc49bed87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
