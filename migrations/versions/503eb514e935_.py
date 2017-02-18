"""empty message

Revision ID: 503eb514e935
Revises: 
Create Date: 2017-02-18 17:16:00.731009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '503eb514e935'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=150), nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), nullable=True),
    sa.Column('username', sa.VARCHAR(length=255), nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), nullable=True),
    sa.Column('is_super_admin', sa.BOOLEAN(), nullable=True),
    sa.Column('role', sa.Enum('teacher', 'student'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###