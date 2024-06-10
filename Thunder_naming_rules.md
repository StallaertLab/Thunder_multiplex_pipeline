## Naming pattern for multiplexed Thunder experiment

pattern:
**ROUND_SCAN_WELL_MARKER1_MARKER2_MARKERn**

where:
- ROUND
	- number of a round 
	- format: '00'
- SCAN
	- number of a scan within a round 
	- used most often when 750 channel has to be imaged separately
	- format: '00' 
- WELL
	- well on a plate
	- format: 'A01'
- MARKER
	- name of the antibody
	- if wavelength is added use hyphen to separate antibody name and the wavelength
	- format: 'RB1' or 'RB1-AF488'

general rules:
- don't use underscore in the name besides as a separating element
- don't use spaces or any other special characters

examples:
'00_00_A01_DAPI_RB-AF488_PLK1-AF555'