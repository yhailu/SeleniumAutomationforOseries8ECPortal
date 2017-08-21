
#from OSeriesAutomationUtilities.Logging import VertexLogger
import FileStructure as _FileStructure
from env import env as _env
import os as _os


#from logging import getLogger
project = "libs"
pkg = "Oseries8"


env = _env(_os.path.join(project, pkg))


_FileStructure.createFileStructure(project, pkg, env)
FileStructure = _FileStructure.getFileStructure()
