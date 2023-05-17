"""change create column

Revision ID: 1569de2d3cf1
Revises: 5d2a2405ddb8
Create Date: 2023-05-18 01:37:29.906115

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1569de2d3cf1'
down_revision = '5d2a2405ddb8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'questions', 'create_date', new_column_name='created_date',
        type_=sa.TEXT()
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'questions', 'created_date', new_column_name='create_date',
        type_=postgresql.TIMESTAMP()
    )
    # ### end Alembic commands ###
