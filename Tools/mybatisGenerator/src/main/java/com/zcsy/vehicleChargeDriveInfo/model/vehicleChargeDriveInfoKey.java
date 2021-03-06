package com.zcsy.vehicleChargeDriveInfo.model;

import java.util.Date;

/**
 *
 * This class was generated by MyBatis Generator.
 * This class corresponds to the database table vehicle_charge_drive_info
 */
public class vehicleChargeDriveInfoKey {
    /**
     * Database Column Remarks:
     *   vin码
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column vehicle_charge_drive_info.vin
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    private String vin;

    /**
     * Database Column Remarks:
     *   数据类型：1-充电数据，2-行驶数据
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column vehicle_charge_drive_info.data_type
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    private Integer dataType;

    /**
     * Database Column Remarks:
     *   开始时间
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column vehicle_charge_drive_info.begin_time
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    private Date beginTime;

    /**
     * Database Column Remarks:
     *   结束时间
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column vehicle_charge_drive_info.end_time
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    private Date endTime;

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column vehicle_charge_drive_info.vin
     *
     * @return the value of vehicle_charge_drive_info.vin
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public String getVin() {
        return vin;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column vehicle_charge_drive_info.vin
     *
     * @param vin the value for vehicle_charge_drive_info.vin
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public void setVin(String vin) {
        this.vin = vin == null ? null : vin.trim();
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column vehicle_charge_drive_info.data_type
     *
     * @return the value of vehicle_charge_drive_info.data_type
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public Integer getDataType() {
        return dataType;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column vehicle_charge_drive_info.data_type
     *
     * @param dataType the value for vehicle_charge_drive_info.data_type
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public void setDataType(Integer dataType) {
        this.dataType = dataType;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column vehicle_charge_drive_info.begin_time
     *
     * @return the value of vehicle_charge_drive_info.begin_time
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public Date getBeginTime() {
        return beginTime;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column vehicle_charge_drive_info.begin_time
     *
     * @param beginTime the value for vehicle_charge_drive_info.begin_time
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public void setBeginTime(Date beginTime) {
        this.beginTime = beginTime;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column vehicle_charge_drive_info.end_time
     *
     * @return the value of vehicle_charge_drive_info.end_time
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public Date getEndTime() {
        return endTime;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column vehicle_charge_drive_info.end_time
     *
     * @param endTime the value for vehicle_charge_drive_info.end_time
     *
     * @mbg.generated Wed Sep 12 15:26:10 CST 2018
     */
    public void setEndTime(Date endTime) {
        this.endTime = endTime;
    }
}