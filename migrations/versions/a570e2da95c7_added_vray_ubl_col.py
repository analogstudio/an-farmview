"""added vray ubl col

Revision ID: a570e2da95c7
Revises: e7d7e542dcad
Create Date: 2023-08-18 14:26:46.577737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a570e2da95c7'
down_revision = 'e7d7e542dcad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ubl', sa.Column('vray_entitled', sa.Integer(), nullable=True))
    op.add_column('ubl', sa.Column('vray_used', sa.Integer(), nullable=True))
    op.add_column('ubl', sa.Column('vray_available', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ubl', 'vray_available')
    op.drop_column('ubl', 'vray_used')
    op.drop_column('ubl', 'vray_entitled')
    # ### end Alembic commands ###
