from hoshino.util import get_environ, get_bool_environ
from .__bot__ import HOST, PORT

ICP_CONTENT = get_environ('ICP_CONTENT')
PUBLIC_ADDRESS = get_environ('PUBLIC_ADDRESS', f"http://{HOST}:{PORT}")
PASSWORD = get_environ('BOT_MANAGER_WEB_PASSWORD', 'l8ViAJBICgU8craR')
ALLOW_PRIVATE = get_bool_environ('ALLOW_PRIVATE', False)
