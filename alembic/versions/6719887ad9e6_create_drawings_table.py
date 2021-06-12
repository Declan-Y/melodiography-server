"""create drawings table

Revision ID: 6719887ad9e6
Revises: 
Create Date: 2021-06-12 23:40:11.409229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6719887ad9e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'drawings',
        sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('title', sa.String)
    )


def downgrade():
    op.drop_table('drawings')
