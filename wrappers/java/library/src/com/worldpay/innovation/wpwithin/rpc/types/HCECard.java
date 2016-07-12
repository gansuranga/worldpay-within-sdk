/**
 * Autogenerated by Thrift Compiler (0.9.3)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package com.worldpay.innovation.wpwithin.rpc.types;

import org.apache.thrift.scheme.IScheme;
import org.apache.thrift.scheme.SchemeFactory;
import org.apache.thrift.scheme.StandardScheme;

import org.apache.thrift.scheme.TupleScheme;
import org.apache.thrift.protocol.TTupleProtocol;
import org.apache.thrift.protocol.TProtocolException;
import org.apache.thrift.EncodingUtils;
import org.apache.thrift.TException;
import org.apache.thrift.async.AsyncMethodCallback;
import org.apache.thrift.server.AbstractNonblockingServer.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.EnumMap;
import java.util.Set;
import java.util.HashSet;
import java.util.EnumSet;
import java.util.Collections;
import java.util.BitSet;
import java.nio.ByteBuffer;
import java.util.Arrays;
import javax.annotation.Generated;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked"})
@Generated(value = "Autogenerated by Thrift Compiler (0.9.3)", date = "2016-07-12")
public class HCECard implements org.apache.thrift.TBase<HCECard, HCECard._Fields>, java.io.Serializable, Cloneable, Comparable<HCECard> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("HCECard");

  private static final org.apache.thrift.protocol.TField FIRST_NAME_FIELD_DESC = new org.apache.thrift.protocol.TField("FirstName", org.apache.thrift.protocol.TType.STRING, (short)1);
  private static final org.apache.thrift.protocol.TField LAST_NAME_FIELD_DESC = new org.apache.thrift.protocol.TField("LastName", org.apache.thrift.protocol.TType.STRING, (short)2);
  private static final org.apache.thrift.protocol.TField EXP_MONTH_FIELD_DESC = new org.apache.thrift.protocol.TField("ExpMonth", org.apache.thrift.protocol.TType.I32, (short)3);
  private static final org.apache.thrift.protocol.TField EXP_YEAR_FIELD_DESC = new org.apache.thrift.protocol.TField("ExpYear", org.apache.thrift.protocol.TType.I32, (short)4);
  private static final org.apache.thrift.protocol.TField CARD_NUMBER_FIELD_DESC = new org.apache.thrift.protocol.TField("CardNumber", org.apache.thrift.protocol.TType.STRING, (short)5);
  private static final org.apache.thrift.protocol.TField TYPE_FIELD_DESC = new org.apache.thrift.protocol.TField("Type", org.apache.thrift.protocol.TType.STRING, (short)6);
  private static final org.apache.thrift.protocol.TField CVC_FIELD_DESC = new org.apache.thrift.protocol.TField("Cvc", org.apache.thrift.protocol.TType.STRING, (short)7);

  private static final Map<Class<? extends IScheme>, SchemeFactory> schemes = new HashMap<Class<? extends IScheme>, SchemeFactory>();
  static {
    schemes.put(StandardScheme.class, new HCECardStandardSchemeFactory());
    schemes.put(TupleScheme.class, new HCECardTupleSchemeFactory());
  }

  public String FirstName; // required
  public String LastName; // required
  public int ExpMonth; // required
  public int ExpYear; // required
  public String CardNumber; // required
  public String Type; // required
  public String Cvc; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    FIRST_NAME((short)1, "FirstName"),
    LAST_NAME((short)2, "LastName"),
    EXP_MONTH((short)3, "ExpMonth"),
    EXP_YEAR((short)4, "ExpYear"),
    CARD_NUMBER((short)5, "CardNumber"),
    TYPE((short)6, "Type"),
    CVC((short)7, "Cvc");

    private static final Map<String, _Fields> byName = new HashMap<String, _Fields>();

    static {
      for (_Fields field : EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // FIRST_NAME
          return FIRST_NAME;
        case 2: // LAST_NAME
          return LAST_NAME;
        case 3: // EXP_MONTH
          return EXP_MONTH;
        case 4: // EXP_YEAR
          return EXP_YEAR;
        case 5: // CARD_NUMBER
          return CARD_NUMBER;
        case 6: // TYPE
          return TYPE;
        case 7: // CVC
          return CVC;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final String _fieldName;

    _Fields(short thriftId, String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  private static final int __EXPMONTH_ISSET_ID = 0;
  private static final int __EXPYEAR_ISSET_ID = 1;
  private byte __isset_bitfield = 0;
  public static final Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.FIRST_NAME, new org.apache.thrift.meta_data.FieldMetaData("FirstName", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.LAST_NAME, new org.apache.thrift.meta_data.FieldMetaData("LastName", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.EXP_MONTH, new org.apache.thrift.meta_data.FieldMetaData("ExpMonth", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.I32)));
    tmpMap.put(_Fields.EXP_YEAR, new org.apache.thrift.meta_data.FieldMetaData("ExpYear", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.I32)));
    tmpMap.put(_Fields.CARD_NUMBER, new org.apache.thrift.meta_data.FieldMetaData("CardNumber", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.TYPE, new org.apache.thrift.meta_data.FieldMetaData("Type", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.CVC, new org.apache.thrift.meta_data.FieldMetaData("Cvc", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    metaDataMap = Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(HCECard.class, metaDataMap);
  }

  public HCECard() {
  }

  public HCECard(
    String FirstName,
    String LastName,
    int ExpMonth,
    int ExpYear,
    String CardNumber,
    String Type,
    String Cvc)
  {
    this();
    this.FirstName = FirstName;
    this.LastName = LastName;
    this.ExpMonth = ExpMonth;
    setExpMonthIsSet(true);
    this.ExpYear = ExpYear;
    setExpYearIsSet(true);
    this.CardNumber = CardNumber;
    this.Type = Type;
    this.Cvc = Cvc;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public HCECard(HCECard other) {
    __isset_bitfield = other.__isset_bitfield;
    if (other.isSetFirstName()) {
      this.FirstName = other.FirstName;
    }
    if (other.isSetLastName()) {
      this.LastName = other.LastName;
    }
    this.ExpMonth = other.ExpMonth;
    this.ExpYear = other.ExpYear;
    if (other.isSetCardNumber()) {
      this.CardNumber = other.CardNumber;
    }
    if (other.isSetType()) {
      this.Type = other.Type;
    }
    if (other.isSetCvc()) {
      this.Cvc = other.Cvc;
    }
  }

  public HCECard deepCopy() {
    return new HCECard(this);
  }

  @Override
  public void clear() {
    this.FirstName = null;
    this.LastName = null;
    setExpMonthIsSet(false);
    this.ExpMonth = 0;
    setExpYearIsSet(false);
    this.ExpYear = 0;
    this.CardNumber = null;
    this.Type = null;
    this.Cvc = null;
  }

  public String getFirstName() {
    return this.FirstName;
  }

  public HCECard setFirstName(String FirstName) {
    this.FirstName = FirstName;
    return this;
  }

  public void unsetFirstName() {
    this.FirstName = null;
  }

  /** Returns true if field FirstName is set (has been assigned a value) and false otherwise */
  public boolean isSetFirstName() {
    return this.FirstName != null;
  }

  public void setFirstNameIsSet(boolean value) {
    if (!value) {
      this.FirstName = null;
    }
  }

  public String getLastName() {
    return this.LastName;
  }

  public HCECard setLastName(String LastName) {
    this.LastName = LastName;
    return this;
  }

  public void unsetLastName() {
    this.LastName = null;
  }

  /** Returns true if field LastName is set (has been assigned a value) and false otherwise */
  public boolean isSetLastName() {
    return this.LastName != null;
  }

  public void setLastNameIsSet(boolean value) {
    if (!value) {
      this.LastName = null;
    }
  }

  public int getExpMonth() {
    return this.ExpMonth;
  }

  public HCECard setExpMonth(int ExpMonth) {
    this.ExpMonth = ExpMonth;
    setExpMonthIsSet(true);
    return this;
  }

  public void unsetExpMonth() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __EXPMONTH_ISSET_ID);
  }

  /** Returns true if field ExpMonth is set (has been assigned a value) and false otherwise */
  public boolean isSetExpMonth() {
    return EncodingUtils.testBit(__isset_bitfield, __EXPMONTH_ISSET_ID);
  }

  public void setExpMonthIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __EXPMONTH_ISSET_ID, value);
  }

  public int getExpYear() {
    return this.ExpYear;
  }

  public HCECard setExpYear(int ExpYear) {
    this.ExpYear = ExpYear;
    setExpYearIsSet(true);
    return this;
  }

  public void unsetExpYear() {
    __isset_bitfield = EncodingUtils.clearBit(__isset_bitfield, __EXPYEAR_ISSET_ID);
  }

  /** Returns true if field ExpYear is set (has been assigned a value) and false otherwise */
  public boolean isSetExpYear() {
    return EncodingUtils.testBit(__isset_bitfield, __EXPYEAR_ISSET_ID);
  }

  public void setExpYearIsSet(boolean value) {
    __isset_bitfield = EncodingUtils.setBit(__isset_bitfield, __EXPYEAR_ISSET_ID, value);
  }

  public String getCardNumber() {
    return this.CardNumber;
  }

  public HCECard setCardNumber(String CardNumber) {
    this.CardNumber = CardNumber;
    return this;
  }

  public void unsetCardNumber() {
    this.CardNumber = null;
  }

  /** Returns true if field CardNumber is set (has been assigned a value) and false otherwise */
  public boolean isSetCardNumber() {
    return this.CardNumber != null;
  }

  public void setCardNumberIsSet(boolean value) {
    if (!value) {
      this.CardNumber = null;
    }
  }

  public String getType() {
    return this.Type;
  }

  public HCECard setType(String Type) {
    this.Type = Type;
    return this;
  }

  public void unsetType() {
    this.Type = null;
  }

  /** Returns true if field Type is set (has been assigned a value) and false otherwise */
  public boolean isSetType() {
    return this.Type != null;
  }

  public void setTypeIsSet(boolean value) {
    if (!value) {
      this.Type = null;
    }
  }

  public String getCvc() {
    return this.Cvc;
  }

  public HCECard setCvc(String Cvc) {
    this.Cvc = Cvc;
    return this;
  }

  public void unsetCvc() {
    this.Cvc = null;
  }

  /** Returns true if field Cvc is set (has been assigned a value) and false otherwise */
  public boolean isSetCvc() {
    return this.Cvc != null;
  }

  public void setCvcIsSet(boolean value) {
    if (!value) {
      this.Cvc = null;
    }
  }

  public void setFieldValue(_Fields field, Object value) {
    switch (field) {
    case FIRST_NAME:
      if (value == null) {
        unsetFirstName();
      } else {
        setFirstName((String)value);
      }
      break;

    case LAST_NAME:
      if (value == null) {
        unsetLastName();
      } else {
        setLastName((String)value);
      }
      break;

    case EXP_MONTH:
      if (value == null) {
        unsetExpMonth();
      } else {
        setExpMonth((Integer)value);
      }
      break;

    case EXP_YEAR:
      if (value == null) {
        unsetExpYear();
      } else {
        setExpYear((Integer)value);
      }
      break;

    case CARD_NUMBER:
      if (value == null) {
        unsetCardNumber();
      } else {
        setCardNumber((String)value);
      }
      break;

    case TYPE:
      if (value == null) {
        unsetType();
      } else {
        setType((String)value);
      }
      break;

    case CVC:
      if (value == null) {
        unsetCvc();
      } else {
        setCvc((String)value);
      }
      break;

    }
  }

  public Object getFieldValue(_Fields field) {
    switch (field) {
    case FIRST_NAME:
      return getFirstName();

    case LAST_NAME:
      return getLastName();

    case EXP_MONTH:
      return getExpMonth();

    case EXP_YEAR:
      return getExpYear();

    case CARD_NUMBER:
      return getCardNumber();

    case TYPE:
      return getType();

    case CVC:
      return getCvc();

    }
    throw new IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new IllegalArgumentException();
    }

    switch (field) {
    case FIRST_NAME:
      return isSetFirstName();
    case LAST_NAME:
      return isSetLastName();
    case EXP_MONTH:
      return isSetExpMonth();
    case EXP_YEAR:
      return isSetExpYear();
    case CARD_NUMBER:
      return isSetCardNumber();
    case TYPE:
      return isSetType();
    case CVC:
      return isSetCvc();
    }
    throw new IllegalStateException();
  }

  @Override
  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof HCECard)
      return this.equals((HCECard)that);
    return false;
  }

  public boolean equals(HCECard that) {
    if (that == null)
      return false;

    boolean this_present_FirstName = true && this.isSetFirstName();
    boolean that_present_FirstName = true && that.isSetFirstName();
    if (this_present_FirstName || that_present_FirstName) {
      if (!(this_present_FirstName && that_present_FirstName))
        return false;
      if (!this.FirstName.equals(that.FirstName))
        return false;
    }

    boolean this_present_LastName = true && this.isSetLastName();
    boolean that_present_LastName = true && that.isSetLastName();
    if (this_present_LastName || that_present_LastName) {
      if (!(this_present_LastName && that_present_LastName))
        return false;
      if (!this.LastName.equals(that.LastName))
        return false;
    }

    boolean this_present_ExpMonth = true;
    boolean that_present_ExpMonth = true;
    if (this_present_ExpMonth || that_present_ExpMonth) {
      if (!(this_present_ExpMonth && that_present_ExpMonth))
        return false;
      if (this.ExpMonth != that.ExpMonth)
        return false;
    }

    boolean this_present_ExpYear = true;
    boolean that_present_ExpYear = true;
    if (this_present_ExpYear || that_present_ExpYear) {
      if (!(this_present_ExpYear && that_present_ExpYear))
        return false;
      if (this.ExpYear != that.ExpYear)
        return false;
    }

    boolean this_present_CardNumber = true && this.isSetCardNumber();
    boolean that_present_CardNumber = true && that.isSetCardNumber();
    if (this_present_CardNumber || that_present_CardNumber) {
      if (!(this_present_CardNumber && that_present_CardNumber))
        return false;
      if (!this.CardNumber.equals(that.CardNumber))
        return false;
    }

    boolean this_present_Type = true && this.isSetType();
    boolean that_present_Type = true && that.isSetType();
    if (this_present_Type || that_present_Type) {
      if (!(this_present_Type && that_present_Type))
        return false;
      if (!this.Type.equals(that.Type))
        return false;
    }

    boolean this_present_Cvc = true && this.isSetCvc();
    boolean that_present_Cvc = true && that.isSetCvc();
    if (this_present_Cvc || that_present_Cvc) {
      if (!(this_present_Cvc && that_present_Cvc))
        return false;
      if (!this.Cvc.equals(that.Cvc))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    List<Object> list = new ArrayList<Object>();

    boolean present_FirstName = true && (isSetFirstName());
    list.add(present_FirstName);
    if (present_FirstName)
      list.add(FirstName);

    boolean present_LastName = true && (isSetLastName());
    list.add(present_LastName);
    if (present_LastName)
      list.add(LastName);

    boolean present_ExpMonth = true;
    list.add(present_ExpMonth);
    if (present_ExpMonth)
      list.add(ExpMonth);

    boolean present_ExpYear = true;
    list.add(present_ExpYear);
    if (present_ExpYear)
      list.add(ExpYear);

    boolean present_CardNumber = true && (isSetCardNumber());
    list.add(present_CardNumber);
    if (present_CardNumber)
      list.add(CardNumber);

    boolean present_Type = true && (isSetType());
    list.add(present_Type);
    if (present_Type)
      list.add(Type);

    boolean present_Cvc = true && (isSetCvc());
    list.add(present_Cvc);
    if (present_Cvc)
      list.add(Cvc);

    return list.hashCode();
  }

  @Override
  public int compareTo(HCECard other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetFirstName()).compareTo(other.isSetFirstName());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetFirstName()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.FirstName, other.FirstName);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetLastName()).compareTo(other.isSetLastName());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetLastName()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.LastName, other.LastName);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetExpMonth()).compareTo(other.isSetExpMonth());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetExpMonth()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.ExpMonth, other.ExpMonth);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetExpYear()).compareTo(other.isSetExpYear());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetExpYear()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.ExpYear, other.ExpYear);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetCardNumber()).compareTo(other.isSetCardNumber());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetCardNumber()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.CardNumber, other.CardNumber);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetType()).compareTo(other.isSetType());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetType()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.Type, other.Type);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = Boolean.valueOf(isSetCvc()).compareTo(other.isSetCvc());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetCvc()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.Cvc, other.Cvc);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    schemes.get(iprot.getScheme()).getScheme().read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    schemes.get(oprot.getScheme()).getScheme().write(oprot, this);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder("HCECard(");
    boolean first = true;

    sb.append("FirstName:");
    if (this.FirstName == null) {
      sb.append("null");
    } else {
      sb.append(this.FirstName);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("LastName:");
    if (this.LastName == null) {
      sb.append("null");
    } else {
      sb.append(this.LastName);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("ExpMonth:");
    sb.append(this.ExpMonth);
    first = false;
    if (!first) sb.append(", ");
    sb.append("ExpYear:");
    sb.append(this.ExpYear);
    first = false;
    if (!first) sb.append(", ");
    sb.append("CardNumber:");
    if (this.CardNumber == null) {
      sb.append("null");
    } else {
      sb.append(this.CardNumber);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("Type:");
    if (this.Type == null) {
      sb.append("null");
    } else {
      sb.append(this.Type);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("Cvc:");
    if (this.Cvc == null) {
      sb.append("null");
    } else {
      sb.append(this.Cvc);
    }
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, ClassNotFoundException {
    try {
      // it doesn't seem like you should have to do this, but java serialization is wacky, and doesn't call the default constructor.
      __isset_bitfield = 0;
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class HCECardStandardSchemeFactory implements SchemeFactory {
    public HCECardStandardScheme getScheme() {
      return new HCECardStandardScheme();
    }
  }

  private static class HCECardStandardScheme extends StandardScheme<HCECard> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, HCECard struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // FIRST_NAME
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.FirstName = iprot.readString();
              struct.setFirstNameIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // LAST_NAME
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.LastName = iprot.readString();
              struct.setLastNameIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // EXP_MONTH
            if (schemeField.type == org.apache.thrift.protocol.TType.I32) {
              struct.ExpMonth = iprot.readI32();
              struct.setExpMonthIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 4: // EXP_YEAR
            if (schemeField.type == org.apache.thrift.protocol.TType.I32) {
              struct.ExpYear = iprot.readI32();
              struct.setExpYearIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 5: // CARD_NUMBER
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.CardNumber = iprot.readString();
              struct.setCardNumberIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 6: // TYPE
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.Type = iprot.readString();
              struct.setTypeIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 7: // CVC
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.Cvc = iprot.readString();
              struct.setCvcIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, HCECard struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.FirstName != null) {
        oprot.writeFieldBegin(FIRST_NAME_FIELD_DESC);
        oprot.writeString(struct.FirstName);
        oprot.writeFieldEnd();
      }
      if (struct.LastName != null) {
        oprot.writeFieldBegin(LAST_NAME_FIELD_DESC);
        oprot.writeString(struct.LastName);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldBegin(EXP_MONTH_FIELD_DESC);
      oprot.writeI32(struct.ExpMonth);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(EXP_YEAR_FIELD_DESC);
      oprot.writeI32(struct.ExpYear);
      oprot.writeFieldEnd();
      if (struct.CardNumber != null) {
        oprot.writeFieldBegin(CARD_NUMBER_FIELD_DESC);
        oprot.writeString(struct.CardNumber);
        oprot.writeFieldEnd();
      }
      if (struct.Type != null) {
        oprot.writeFieldBegin(TYPE_FIELD_DESC);
        oprot.writeString(struct.Type);
        oprot.writeFieldEnd();
      }
      if (struct.Cvc != null) {
        oprot.writeFieldBegin(CVC_FIELD_DESC);
        oprot.writeString(struct.Cvc);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class HCECardTupleSchemeFactory implements SchemeFactory {
    public HCECardTupleScheme getScheme() {
      return new HCECardTupleScheme();
    }
  }

  private static class HCECardTupleScheme extends TupleScheme<HCECard> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, HCECard struct) throws org.apache.thrift.TException {
      TTupleProtocol oprot = (TTupleProtocol) prot;
      BitSet optionals = new BitSet();
      if (struct.isSetFirstName()) {
        optionals.set(0);
      }
      if (struct.isSetLastName()) {
        optionals.set(1);
      }
      if (struct.isSetExpMonth()) {
        optionals.set(2);
      }
      if (struct.isSetExpYear()) {
        optionals.set(3);
      }
      if (struct.isSetCardNumber()) {
        optionals.set(4);
      }
      if (struct.isSetType()) {
        optionals.set(5);
      }
      if (struct.isSetCvc()) {
        optionals.set(6);
      }
      oprot.writeBitSet(optionals, 7);
      if (struct.isSetFirstName()) {
        oprot.writeString(struct.FirstName);
      }
      if (struct.isSetLastName()) {
        oprot.writeString(struct.LastName);
      }
      if (struct.isSetExpMonth()) {
        oprot.writeI32(struct.ExpMonth);
      }
      if (struct.isSetExpYear()) {
        oprot.writeI32(struct.ExpYear);
      }
      if (struct.isSetCardNumber()) {
        oprot.writeString(struct.CardNumber);
      }
      if (struct.isSetType()) {
        oprot.writeString(struct.Type);
      }
      if (struct.isSetCvc()) {
        oprot.writeString(struct.Cvc);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, HCECard struct) throws org.apache.thrift.TException {
      TTupleProtocol iprot = (TTupleProtocol) prot;
      BitSet incoming = iprot.readBitSet(7);
      if (incoming.get(0)) {
        struct.FirstName = iprot.readString();
        struct.setFirstNameIsSet(true);
      }
      if (incoming.get(1)) {
        struct.LastName = iprot.readString();
        struct.setLastNameIsSet(true);
      }
      if (incoming.get(2)) {
        struct.ExpMonth = iprot.readI32();
        struct.setExpMonthIsSet(true);
      }
      if (incoming.get(3)) {
        struct.ExpYear = iprot.readI32();
        struct.setExpYearIsSet(true);
      }
      if (incoming.get(4)) {
        struct.CardNumber = iprot.readString();
        struct.setCardNumberIsSet(true);
      }
      if (incoming.get(5)) {
        struct.Type = iprot.readString();
        struct.setTypeIsSet(true);
      }
      if (incoming.get(6)) {
        struct.Cvc = iprot.readString();
        struct.setCvcIsSet(true);
      }
    }
  }

}

