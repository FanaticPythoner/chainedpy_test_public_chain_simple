
# Dual import strategy for Pylance and runtime compatibility, otherwise linting issues

from chainedpy.chain import Chain

from importlib import import_module
import pkgutil, pathlib

# auto-import project plugins on import -------------------------
_plugins_dir = pathlib.Path(__file__).with_suffix('').parent / 'plugins'
for subdir in ['then', 'as_', 'processors']:
    subdir_path = _plugins_dir / subdir
    if subdir_path.exists():
        for mod in pkgutil.iter_modules([str(subdir_path)]):
            if not mod.name.startswith('_'):
                import_module(f'{__package__}.plugins.{subdir}.' + mod.name)

__all__ = ('Chain',)
