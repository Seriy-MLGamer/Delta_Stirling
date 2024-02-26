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

from math import *

exchanger_width=.1
exchanger_height=.1
exchanger_folds=20
exchanger_thickness=.0005
piston_radius=.01
piston_height=.01
cooler_temperature=273
heater_temperature=1000
temperature_drop_coefficient=.9
gas_conductiveness=.0244
gas_capacity=800
gas_pressure=101325
gas_density=1.2929

exchanger_area=exchanger_width*exchanger_height*exchanger_folds
exchanger_volume=exchanger_area*exchanger_thickness
piston_area=pi*piston_radius*piston_radius
piston_volume=piston_area*piston_height
gas_mass=gas_density*exchanger_volume
cooler_gas_pressure=gas_pressure*cooler_temperature/273
heater_gas_pressure=gas_pressure*heater_temperature/273
heater_power=exchanger_volume/(exchanger_volume+piston_volume/2)*gas_conductiveness*exchanger_area*heater_temperature*(1-temperature_drop_coefficient)/exchanger_thickness
print("Exchanger volume:", exchanger_volume, "m**3")
print("Piston volume:", piston_volume, "m**3")
print("Drop:", heater_temperature*temperature_drop_coefficient, "K")
print("Heater power:", 2*heater_power, "W")
print("Temperature speed:", heater_power/(gas_capacity*gas_mass), "K/s")
print("Piston speed:", heater_power/(heater_gas_pressure*piston_area), "m/s")
print("RPM:", heater_power/(heater_gas_pressure*piston_area)/(2*pi*piston_height)*60)