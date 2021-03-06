"""data table

Revision ID: f9e317e504ac
Revises: 
Create Date: 2019-10-13 20:32:27.274775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9e317e504ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('temp', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_date'), 'data', ['date'], unique=True)
    op.create_index(op.f('ix_data_temp'), 'data', ['temp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_data_temp'), table_name='data')
    op.drop_index(op.f('ix_data_date'), table_name='data')
    op.drop_table('data')
    # ### end Alembic commands ###
