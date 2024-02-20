"""add phone number

Revision ID: 377e2ea55d62
Revises: 4be344743f90
Create Date: 2024-01-27 11:40:02.055534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '377e2ea55d62'
down_revision: Union[str, None] = '4be344743f90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_column('users', 'phone_number')
    pass
