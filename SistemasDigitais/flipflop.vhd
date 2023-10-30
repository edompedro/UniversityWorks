library ieee;
use ieee.std_logic_1164.all;

--entidades

entity flipflop is
port(D, CLK, SX, SY, W, store, zeros : in std_logic;
						  Q : out std_logic);
end flipflop;

--comportamento

architecture comportamento of flipflop is

--sinais
signal saida : std_logic;

begin 

process(CLK)
begin
	if(rising_edge(CLK)) then
		if(W = '1' and SX = '1' and SY = '1') then
			q <= store;
		elsif((W = '0') and (SX = '1') and (SY = '1')) then
			Q <= D;
		else 
			q <= zeros;
		end if;
	end if;
end process;
		
end comportamento;