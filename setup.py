import cx_Freeze
from os import listdir, path

dir = path.dirname(__file__)

mypath = 'C:/Users/Liwia/Desktop/CU_10/Data/'
listOffiles = [f for f in listdir(mypath)] 

newlistOffiles = []
for i in listOffiles:
    newlistOffiles.append('Data/' + str(i))

executables = [cx_Freeze.Executable("cannibara.py")]

cx_Freeze.setup(targetName = "CannibaraVsUndead", author = "LL", version = "0.3", options = {"build_exe": {"packages":["pygame", "time", "random", "tkinter", "os", "sys", "math", "random"],
                           "include_files":[f for f in newlistOffiles]}}, description = "Harambe_nie_byl_tylko_gorylem", executables = executables)          
                           #"include_files":["Data\capybara.png", "Data\capybaraUltra.png", "Data\capybaraDead.png", "Data\capybaraDeadRed.png", "Data\cucumberSlice.png", "Data\laser.png", "Data\laser_beam.png", "Data\capybara_barks_mono.wav", "Data\capybara_sound_mono.wav", "Data\KenzoRegularItalic.otf", "Data\Kenzo.otf"]}}, description = "Harambe_nie_byl_tylko_gorylem", executables = executables)                         