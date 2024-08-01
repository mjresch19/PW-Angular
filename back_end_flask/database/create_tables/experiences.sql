CREATE TABLE IF NOT EXISTS `experiences` (
`experience_id`     int(11)    NOT NULL AUTO_INCREMENT 	COMMENT 'The comment id',
`position_id`       int(11)  NOT NULL                   COMMENT 'FK: The name of the commentor',
`name`              varchar(100)  NOT NULL              COMMENT 'The name of the experience',
`description`       varchar(500)  NOT NULL              COMMENT 'The description of the experience',
`hyperlink`         varchar(100)  DEFAULT NULL          COMMENT 'The hyperlink associated with the experience',
`start_date`        varchar(100)  NOT NULL              COMMENT 'The start date of the experience',
`end_date`          varchar(100)  DEFAULT NULL          COMMENT 'The end date of the experience',
PRIMARY KEY  (`experience_id`),
FOREIGN KEY (position_id) REFERENCES positions(position_id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT="Feedback content I have received";