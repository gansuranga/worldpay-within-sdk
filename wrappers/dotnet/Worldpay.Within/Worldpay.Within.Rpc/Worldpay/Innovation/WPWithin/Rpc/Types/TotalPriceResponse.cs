/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using Thrift;
using Thrift.Collections;
using System.Runtime.Serialization;
using Thrift.Protocol;
using Thrift.Transport;

namespace Worldpay.Innovation.WPWithin.Rpc.Types
{

  #if !SILVERLIGHT
  [Serializable]
  #endif
  public partial class TotalPriceResponse : TBase
  {

    public string ServerId { get; set; }

    public string ClientId { get; set; }

    public int? PriceId { get; set; }

    public int? UnitsToSupply { get; set; }

    public int? TotalPrice { get; set; }

    public string PaymentReferenceId { get; set; }

    public string MerchantClientKey { get; set; }

    public string CurrencyCode { get; set; }

    public TotalPriceResponse() {
    }

    public void Read (TProtocol iprot)
    {
      iprot.IncrementRecursionDepth();
      try
      {
        TField field;
        iprot.ReadStructBegin();
        while (true)
        {
          field = iprot.ReadFieldBegin();
          if (field.Type == TType.Stop) { 
            break;
          }
          switch (field.ID)
          {
            case 1:
              if (field.Type == TType.String) {
                ServerId = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 2:
              if (field.Type == TType.String) {
                ClientId = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 3:
              if (field.Type == TType.I32) {
                PriceId = iprot.ReadI32();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 4:
              if (field.Type == TType.I32) {
                UnitsToSupply = iprot.ReadI32();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 5:
              if (field.Type == TType.I32) {
                TotalPrice = iprot.ReadI32();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 6:
              if (field.Type == TType.String) {
                PaymentReferenceId = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 7:
              if (field.Type == TType.String) {
                MerchantClientKey = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            case 8:
              if (field.Type == TType.String) {
                CurrencyCode = iprot.ReadString();
              } else { 
                TProtocolUtil.Skip(iprot, field.Type);
              }
              break;
            default: 
              TProtocolUtil.Skip(iprot, field.Type);
              break;
          }
          iprot.ReadFieldEnd();
        }
        iprot.ReadStructEnd();
      }
      finally
      {
        iprot.DecrementRecursionDepth();
      }
    }

    public void Write(TProtocol oprot) {
      oprot.IncrementRecursionDepth();
      try
      {
        TStruct struc = new TStruct("TotalPriceResponse");
        oprot.WriteStructBegin(struc);
        TField field = new TField();
        if (ServerId != null) {
          field.Name = "serverId";
          field.Type = TType.String;
          field.ID = 1;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(ServerId);
          oprot.WriteFieldEnd();
        }
        if (ClientId != null) {
          field.Name = "clientId";
          field.Type = TType.String;
          field.ID = 2;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(ClientId);
          oprot.WriteFieldEnd();
        }
        if (PriceId != null) {
          field.Name = "priceId";
          field.Type = TType.I32;
          field.ID = 3;
          oprot.WriteFieldBegin(field);
          oprot.WriteI32(PriceId.Value);
          oprot.WriteFieldEnd();
        }
        if (UnitsToSupply != null) {
          field.Name = "unitsToSupply";
          field.Type = TType.I32;
          field.ID = 4;
          oprot.WriteFieldBegin(field);
          oprot.WriteI32(UnitsToSupply.Value);
          oprot.WriteFieldEnd();
        }
        if (TotalPrice != null) {
          field.Name = "totalPrice";
          field.Type = TType.I32;
          field.ID = 5;
          oprot.WriteFieldBegin(field);
          oprot.WriteI32(TotalPrice.Value);
          oprot.WriteFieldEnd();
        }
        if (PaymentReferenceId != null) {
          field.Name = "paymentReferenceId";
          field.Type = TType.String;
          field.ID = 6;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(PaymentReferenceId);
          oprot.WriteFieldEnd();
        }
        if (MerchantClientKey != null) {
          field.Name = "merchantClientKey";
          field.Type = TType.String;
          field.ID = 7;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(MerchantClientKey);
          oprot.WriteFieldEnd();
        }
        if (CurrencyCode != null) {
          field.Name = "currencyCode";
          field.Type = TType.String;
          field.ID = 8;
          oprot.WriteFieldBegin(field);
          oprot.WriteString(CurrencyCode);
          oprot.WriteFieldEnd();
        }
        oprot.WriteFieldStop();
        oprot.WriteStructEnd();
      }
      finally
      {
        oprot.DecrementRecursionDepth();
      }
    }

    public override string ToString() {
      StringBuilder __sb = new StringBuilder("TotalPriceResponse(");
      bool __first = true;
      if (ServerId != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("ServerId: ");
        __sb.Append(ServerId);
      }
      if (ClientId != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("ClientId: ");
        __sb.Append(ClientId);
      }
      if (PriceId != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("PriceId: ");
        __sb.Append(PriceId);
      }
      if (UnitsToSupply != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("UnitsToSupply: ");
        __sb.Append(UnitsToSupply);
      }
      if (TotalPrice != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("TotalPrice: ");
        __sb.Append(TotalPrice);
      }
      if (PaymentReferenceId != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("PaymentReferenceId: ");
        __sb.Append(PaymentReferenceId);
      }
      if (MerchantClientKey != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("MerchantClientKey: ");
        __sb.Append(MerchantClientKey);
      }
      if (CurrencyCode != null) {
        if(!__first) { __sb.Append(", "); }
        __first = false;
        __sb.Append("CurrencyCode: ");
        __sb.Append(CurrencyCode);
      }
      __sb.Append(")");
      return __sb.ToString();
    }

  }

}
