"""add content column to posts table

Revision ID: 88ca4188b6c4
Revises: 6880e4296e07
Create Date: 2024-01-27 10:26:30.746134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88ca4188b6c4'
down_revision: Union[str, None] = '6880e4296e07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
