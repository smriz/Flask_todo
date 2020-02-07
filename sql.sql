 CREATE TABLE `list` (   `id` int(11) NOT NULL,   `TODO` varchar(255) NOT NULL,   `status` varchar(255) NOT NULL, `status_flag` int(1) NOT NULL,  `date` date ENGINE=MyISAM DEFAULT CHARSET=latin1;


ALTER TABLE `list`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `list`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
