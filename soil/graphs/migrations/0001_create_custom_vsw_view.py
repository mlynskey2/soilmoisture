# Generated by Django 2.2.1 on 2019-07-28 23:23

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [('skeleton', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            '''
            --VSW = Count * Slope + Intercept
            -- When Period from and to are sorted add --(skeleton_reading.date > skeleton_calibration.period_from AND
            -- skeleton_reading.date < COALESCE(skeleton_calibration.period_to, now()))
            CREATE OR REPLACE VIEW graphs_vsw AS
            SELECT
            	zone1.date,
                zone1.id AS site_id,
                zone1.farm_id,
                zone1.crop_id,
                zone1.type_id AS reading_type_id,

            	zone1.depth1,
            	zone1.count1,
            	zone1.vsw1,

            	zone2.depth2,
            	zone2.count2,
            	zone2.vsw2,

            	zone3.depth3,
            	zone3.count3,
            	zone3.vsw3,

            	zone4.depth4,
            	zone4.count4,
            	zone4.vsw4,

            	zone5.depth5,
            	zone5.count5,
            	zone5.vsw5,

            	zone6.depth6,
            	zone6.count6,
            	zone6.vsw6,

            	zone7.depth7,
            	zone7.count7,
            	zone7.vsw7,

            	zone8.depth8,
            	zone8.count8,
            	zone8.vsw8
            FROM
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
                    skeleton_site.farm_id,
                    skeleton_site.crop_id,
            		skeleton_site.depth1,

            		skeleton_reading.depth1 AS count1,
            		skeleton_calibration.slope AS slope1,
            		skeleton_calibration.intercept AS intercept1,
            		skeleton_reading.depth1 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw1
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he1
            	LEFT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone1"
            ---------
            LEFT JOIN
            --------
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
            		skeleton_site.depth2,

            		skeleton_reading.depth2 AS count2,
            		skeleton_calibration.slope AS slope2,
            		skeleton_calibration.intercept AS intercept2,
            		skeleton_reading.depth2 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw2
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he2
            	LEFT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone2"
            ON zone1.date = zone2.date AND zone1.id = zone2.id
            ---------
            LEFT JOIN
            --------
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
            		skeleton_site.depth3,

            		skeleton_reading.depth3 AS count3,
            		skeleton_calibration.slope AS slope3,
            		skeleton_calibration.intercept AS intercept3,
            		skeleton_reading.depth3 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw3
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he3
            	LEFT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone3"
            ON zone1.date = zone3.date AND zone1.id = zone3.id
            ---------
            LEFT JOIN
            --------
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
            		skeleton_site.depth4,

            		skeleton_reading.depth4 AS count4,
            		skeleton_calibration.slope AS slope4,
            		skeleton_calibration.intercept AS intercept4,
            		skeleton_reading.depth4 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw4
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he4
            	LEFT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone4"
            ON zone1.date = zone4.date AND zone1.id = zone4.id
            ---------
            LEFT JOIN
            --------
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
            		skeleton_site.depth5,

            		skeleton_reading.depth5 AS count5,
            		skeleton_calibration.slope AS slope5,
            		skeleton_calibration.intercept AS intercept5,
            		skeleton_reading.depth5 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw5
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he5
            	LEFT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone5"
            ON zone1.date = zone5.date AND zone1.id = zone5.id
            ---------
            LEFT JOIN
            --------
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
            		skeleton_site.depth6,

            		skeleton_reading.depth6 AS count6,
            		skeleton_calibration.slope AS slope6,
            		skeleton_calibration.intercept AS intercept6,
            		skeleton_reading.depth6 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw6
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he6
            	LEFT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone6"
            ON zone1.date = zone6.date AND zone1.id = zone6.id
            ---------
            LEFT JOIN
            --------
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
            		skeleton_site.depth7,

            		skeleton_reading.depth7 AS count7,
            		skeleton_calibration.slope AS slope7,
            		skeleton_calibration.intercept AS intercept7,
            		skeleton_reading.depth7 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw7
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he7
            	LEFT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone7"
            ON zone1.date = zone7.date AND zone1.id = zone7.id
            ---------
            LEFT JOIN
            --------
            (
            	SELECT
            		skeleton_reading.date,
            		skeleton_site.id,
            		skeleton_reading.type_id,
            		skeleton_site.depth8,

            		skeleton_reading.depth8 AS count8,
            		skeleton_calibration.slope AS slope8,
            		skeleton_calibration.intercept AS intercept8,
            		skeleton_reading.depth8 * skeleton_calibration.slope + skeleton_calibration.intercept AS vsw8
            	FROM
            		skeleton_site
            	LEFT JOIN skeleton_calibration ON skeleton_calibration.soil_type = skeleton_site.depth_he8
            	RIGHT JOIN skeleton_reading ON skeleton_reading.site_id = skeleton_site.id AND skeleton_reading.serial_number_id = skeleton_calibration.serial_number_id
            	WHERE
            		skeleton_reading.type_id = 1 -- Probe
            ) AS "zone8"
            ON zone1.date = zone8.date AND zone1.id = zone8.id
'''

        )

    ]
