#(C) 2024 Серый MLGamer. All freedoms preserved.
#Дзен: <https://dzen.ru/seriy_mlgamer>
#SoundCloud: <https://soundcloud.com/seriy_mlgamer>
#YouTube: <https://www.youtube.com/@Seriy_MLGamer>
#GitHub: <https://github.com/Seriy-MLGamer>
#E-mail: <Seriy-MLGamer@yandex.ru>
#
#This file is part of Delta Stirling.
#Delta Stirling is free work: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#Delta Stirling is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with Delta Stirling. If not, see <https://www.gnu.org/licenses/>.

#Working pistons are in the middle of the stroke, exchangers pistons are at the dead point.

from math import *

exchanger_width=.099-.0045-.005 #Empty exchanger width minus exchanger piston.
exchanger_height=.098
exchanger_folds=20
exchanger_thickness=.0005
piston_radius=.015
piston_stroke=.01
cooler_temperature=293
heater_temperature=1273
temperature_drop_coefficient=.935
gas_conductiveness=.0244
gas_capacity=800
gas_pressure=101325
gas_density=1.2929

exchanger_area=exchanger_width*exchanger_height*exchanger_folds
exchanger_volume=exchanger_area*exchanger_thickness
piston_area=pi*piston_radius**2
cylinder_volume=piston_area*piston_stroke
cooler_gas_pressure=gas_pressure*cooler_temperature/(temperature_drop_coefficient*273)
heater_gas_pressure=gas_pressure*heater_temperature*temperature_drop_coefficient/273
gas_mass=gas_density*exchanger_volume
#Data from "thermodynamics.pixi" file at 100 microseconds.
heater_power=(1191.6193-heater_temperature*temperature_drop_coefficient)*gas_capacity*gas_mass*1000000/100
efficiency=(heater_temperature*temperature_drop_coefficient-cooler_temperature/temperature_drop_coefficient)/(heater_temperature*temperature_drop_coefficient)-.2 #Minus 20% due to various design things.
piston_speed=heater_power/(heater_gas_pressure*piston_area)
print("Exchanger area:", 2*exchanger_area, "m**2")
print("Exchanger volume:", exchanger_volume, "m**3")
print("Piston volume:", cylinder_volume, "m**3")
print("Exchanger to cylinder ratio:", exchanger_volume/cylinder_volume)
print("Cooler temperature:", cooler_temperature, "K")
print("Heater temperature:", heater_temperature, "K")
print("Cooler gas temperature:", cooler_temperature/temperature_drop_coefficient, "K")
print("Heater gas temperature:", heater_temperature*temperature_drop_coefficient, "K")
print("Heater power:", heater_power, "W")
print("Temperature speed:", heater_power/(gas_capacity*gas_mass), "K/s")
print("Efficiency: %i%%"%(efficiency*100))
print("Power:", efficiency*heater_power, "W")
print("Piston speed:", piston_speed, "m/s")
print("RPM:", piston_speed/(pi*piston_stroke)*60)