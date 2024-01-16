-- Displays the max temperature of each state (ordered by State name).

SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP By `state`
ORDER BY `max_temp` DESC;
