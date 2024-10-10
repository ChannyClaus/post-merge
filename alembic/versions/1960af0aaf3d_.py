"""empty message

Revision ID: 1960af0aaf3d
Revises: ea949c1f8747
Create Date: 2024-10-10 01:45:25.861437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1960af0aaf3d'
down_revision: Union[str, None] = 'ea949c1f8747'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
