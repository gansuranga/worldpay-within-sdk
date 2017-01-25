//
// Autogenerated by Thrift Compiler (0.10.0)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//
"use strict";

var thrift = require('thrift');
var Thrift = thrift.Thrift;
var Q = thrift.Q;

var wptypes_ttypes = require('./wptypes_types');


var ttypes = require('./wpwithin_types');
//HELPER FUNCTIONS AND STRUCTURES

var WPWithinCallback_beginServiceDelivery_args = function(args) {
  this.serviceID = null;
  this.serviceDeliveryToken = null;
  this.unitsToSupply = null;
  if (args) {
    if (args.serviceID !== undefined && args.serviceID !== null) {
      this.serviceID = args.serviceID;
    }
    if (args.serviceDeliveryToken !== undefined && args.serviceDeliveryToken !== null) {
      this.serviceDeliveryToken = new wptypes_ttypes.ServiceDeliveryToken(args.serviceDeliveryToken);
    }
    if (args.unitsToSupply !== undefined && args.unitsToSupply !== null) {
      this.unitsToSupply = args.unitsToSupply;
    }
  }
};
WPWithinCallback_beginServiceDelivery_args.prototype = {};
WPWithinCallback_beginServiceDelivery_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.I32) {
        this.serviceID = input.readI32();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRUCT) {
        this.serviceDeliveryToken = new wptypes_ttypes.ServiceDeliveryToken();
        this.serviceDeliveryToken.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.I32) {
        this.unitsToSupply = input.readI32();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

WPWithinCallback_beginServiceDelivery_args.prototype.write = function(output) {
  output.writeStructBegin('WPWithinCallback_beginServiceDelivery_args');
  if (this.serviceID !== null && this.serviceID !== undefined) {
    output.writeFieldBegin('serviceID', Thrift.Type.I32, 1);
    output.writeI32(this.serviceID);
    output.writeFieldEnd();
  }
  if (this.serviceDeliveryToken !== null && this.serviceDeliveryToken !== undefined) {
    output.writeFieldBegin('serviceDeliveryToken', Thrift.Type.STRUCT, 2);
    this.serviceDeliveryToken.write(output);
    output.writeFieldEnd();
  }
  if (this.unitsToSupply !== null && this.unitsToSupply !== undefined) {
    output.writeFieldBegin('unitsToSupply', Thrift.Type.I32, 3);
    output.writeI32(this.unitsToSupply);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var WPWithinCallback_beginServiceDelivery_result = function(args) {
  this.err = null;
  if (args instanceof wptypes_ttypes.Error) {
    this.err = args;
    return;
  }
  if (args) {
    if (args.err !== undefined && args.err !== null) {
      this.err = args.err;
    }
  }
};
WPWithinCallback_beginServiceDelivery_result.prototype = {};
WPWithinCallback_beginServiceDelivery_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.err = new wptypes_ttypes.Error();
        this.err.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

WPWithinCallback_beginServiceDelivery_result.prototype.write = function(output) {
  output.writeStructBegin('WPWithinCallback_beginServiceDelivery_result');
  if (this.err !== null && this.err !== undefined) {
    output.writeFieldBegin('err', Thrift.Type.STRUCT, 1);
    this.err.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var WPWithinCallback_endServiceDelivery_args = function(args) {
  this.serviceID = null;
  this.serviceDeliveryToken = null;
  this.unitsReceived = null;
  if (args) {
    if (args.serviceID !== undefined && args.serviceID !== null) {
      this.serviceID = args.serviceID;
    }
    if (args.serviceDeliveryToken !== undefined && args.serviceDeliveryToken !== null) {
      this.serviceDeliveryToken = new wptypes_ttypes.ServiceDeliveryToken(args.serviceDeliveryToken);
    }
    if (args.unitsReceived !== undefined && args.unitsReceived !== null) {
      this.unitsReceived = args.unitsReceived;
    }
  }
};
WPWithinCallback_endServiceDelivery_args.prototype = {};
WPWithinCallback_endServiceDelivery_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.I32) {
        this.serviceID = input.readI32();
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRUCT) {
        this.serviceDeliveryToken = new wptypes_ttypes.ServiceDeliveryToken();
        this.serviceDeliveryToken.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 3:
      if (ftype == Thrift.Type.I32) {
        this.unitsReceived = input.readI32();
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

WPWithinCallback_endServiceDelivery_args.prototype.write = function(output) {
  output.writeStructBegin('WPWithinCallback_endServiceDelivery_args');
  if (this.serviceID !== null && this.serviceID !== undefined) {
    output.writeFieldBegin('serviceID', Thrift.Type.I32, 1);
    output.writeI32(this.serviceID);
    output.writeFieldEnd();
  }
  if (this.serviceDeliveryToken !== null && this.serviceDeliveryToken !== undefined) {
    output.writeFieldBegin('serviceDeliveryToken', Thrift.Type.STRUCT, 2);
    this.serviceDeliveryToken.write(output);
    output.writeFieldEnd();
  }
  if (this.unitsReceived !== null && this.unitsReceived !== undefined) {
    output.writeFieldBegin('unitsReceived', Thrift.Type.I32, 3);
    output.writeI32(this.unitsReceived);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var WPWithinCallback_endServiceDelivery_result = function(args) {
  this.err = null;
  if (args instanceof wptypes_ttypes.Error) {
    this.err = args;
    return;
  }
  if (args) {
    if (args.err !== undefined && args.err !== null) {
      this.err = args.err;
    }
  }
};
WPWithinCallback_endServiceDelivery_result.prototype = {};
WPWithinCallback_endServiceDelivery_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.err = new wptypes_ttypes.Error();
        this.err.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

WPWithinCallback_endServiceDelivery_result.prototype.write = function(output) {
  output.writeStructBegin('WPWithinCallback_endServiceDelivery_result');
  if (this.err !== null && this.err !== undefined) {
    output.writeFieldBegin('err', Thrift.Type.STRUCT, 1);
    this.err.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

var WPWithinCallbackClient = exports.Client = function(output, pClass) {
    this.output = output;
    this.pClass = pClass;
    this._seqid = 0;
    this._reqs = {};
};
WPWithinCallbackClient.prototype = {};
WPWithinCallbackClient.prototype.seqid = function() { return this._seqid; };
WPWithinCallbackClient.prototype.new_seqid = function() { return this._seqid += 1; };
WPWithinCallbackClient.prototype.beginServiceDelivery = function(serviceID, serviceDeliveryToken, unitsToSupply, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_beginServiceDelivery(serviceID, serviceDeliveryToken, unitsToSupply);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_beginServiceDelivery(serviceID, serviceDeliveryToken, unitsToSupply);
  }
};

WPWithinCallbackClient.prototype.send_beginServiceDelivery = function(serviceID, serviceDeliveryToken, unitsToSupply) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('beginServiceDelivery', Thrift.MessageType.CALL, this.seqid());
  var args = new WPWithinCallback_beginServiceDelivery_args();
  args.serviceID = serviceID;
  args.serviceDeliveryToken = serviceDeliveryToken;
  args.unitsToSupply = unitsToSupply;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

WPWithinCallbackClient.prototype.recv_beginServiceDelivery = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new WPWithinCallback_beginServiceDelivery_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.err) {
    return callback(result.err);
  }
  callback(null);
};
WPWithinCallbackClient.prototype.endServiceDelivery = function(serviceID, serviceDeliveryToken, unitsReceived, callback) {
  this._seqid = this.new_seqid();
  if (callback === undefined) {
    var _defer = Q.defer();
    this._reqs[this.seqid()] = function(error, result) {
      if (error) {
        _defer.reject(error);
      } else {
        _defer.resolve(result);
      }
    };
    this.send_endServiceDelivery(serviceID, serviceDeliveryToken, unitsReceived);
    return _defer.promise;
  } else {
    this._reqs[this.seqid()] = callback;
    this.send_endServiceDelivery(serviceID, serviceDeliveryToken, unitsReceived);
  }
};

WPWithinCallbackClient.prototype.send_endServiceDelivery = function(serviceID, serviceDeliveryToken, unitsReceived) {
  var output = new this.pClass(this.output);
  output.writeMessageBegin('endServiceDelivery', Thrift.MessageType.CALL, this.seqid());
  var args = new WPWithinCallback_endServiceDelivery_args();
  args.serviceID = serviceID;
  args.serviceDeliveryToken = serviceDeliveryToken;
  args.unitsReceived = unitsReceived;
  args.write(output);
  output.writeMessageEnd();
  return this.output.flush();
};

WPWithinCallbackClient.prototype.recv_endServiceDelivery = function(input,mtype,rseqid) {
  var callback = this._reqs[rseqid] || function() {};
  delete this._reqs[rseqid];
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(input);
    input.readMessageEnd();
    return callback(x);
  }
  var result = new WPWithinCallback_endServiceDelivery_result();
  result.read(input);
  input.readMessageEnd();

  if (null !== result.err) {
    return callback(result.err);
  }
  callback(null);
};
var WPWithinCallbackProcessor = exports.Processor = function(handler) {
  this._handler = handler;
}
;
WPWithinCallbackProcessor.prototype.process = function(input, output) {
  var r = input.readMessageBegin();
  if (this['process_' + r.fname]) {
    return this['process_' + r.fname].call(this, r.rseqid, input, output);
  } else {
    input.skip(Thrift.Type.STRUCT);
    input.readMessageEnd();
    var x = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN_METHOD, 'Unknown function ' + r.fname);
    output.writeMessageBegin(r.fname, Thrift.MessageType.EXCEPTION, r.rseqid);
    x.write(output);
    output.writeMessageEnd();
    output.flush();
  }
}
;
WPWithinCallbackProcessor.prototype.process_beginServiceDelivery = function(seqid, input, output) {
  var args = new WPWithinCallback_beginServiceDelivery_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.beginServiceDelivery.length === 3) {
    Q.fcall(this._handler.beginServiceDelivery, args.serviceID, args.serviceDeliveryToken, args.unitsToSupply)
      .then(function(result) {
        var result_obj = new WPWithinCallback_beginServiceDelivery_result({success: result});
        output.writeMessageBegin("beginServiceDelivery", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        if (err instanceof wptypes_ttypes.Error) {
          result = new WPWithinCallback_beginServiceDelivery_result(err);
          output.writeMessageBegin("beginServiceDelivery", Thrift.MessageType.REPLY, seqid);
        } else {
          result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
          output.writeMessageBegin("beginServiceDelivery", Thrift.MessageType.EXCEPTION, seqid);
        }
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.beginServiceDelivery(args.serviceID, args.serviceDeliveryToken, args.unitsToSupply, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined') || err instanceof wptypes_ttypes.Error) {
        result_obj = new WPWithinCallback_beginServiceDelivery_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("beginServiceDelivery", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("beginServiceDelivery", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
WPWithinCallbackProcessor.prototype.process_endServiceDelivery = function(seqid, input, output) {
  var args = new WPWithinCallback_endServiceDelivery_args();
  args.read(input);
  input.readMessageEnd();
  if (this._handler.endServiceDelivery.length === 3) {
    Q.fcall(this._handler.endServiceDelivery, args.serviceID, args.serviceDeliveryToken, args.unitsReceived)
      .then(function(result) {
        var result_obj = new WPWithinCallback_endServiceDelivery_result({success: result});
        output.writeMessageBegin("endServiceDelivery", Thrift.MessageType.REPLY, seqid);
        result_obj.write(output);
        output.writeMessageEnd();
        output.flush();
      }, function (err) {
        var result;
        if (err instanceof wptypes_ttypes.Error) {
          result = new WPWithinCallback_endServiceDelivery_result(err);
          output.writeMessageBegin("endServiceDelivery", Thrift.MessageType.REPLY, seqid);
        } else {
          result = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
          output.writeMessageBegin("endServiceDelivery", Thrift.MessageType.EXCEPTION, seqid);
        }
        result.write(output);
        output.writeMessageEnd();
        output.flush();
      });
  } else {
    this._handler.endServiceDelivery(args.serviceID, args.serviceDeliveryToken, args.unitsReceived, function (err, result) {
      var result_obj;
      if ((err === null || typeof err === 'undefined') || err instanceof wptypes_ttypes.Error) {
        result_obj = new WPWithinCallback_endServiceDelivery_result((err !== null || typeof err === 'undefined') ? err : {success: result});
        output.writeMessageBegin("endServiceDelivery", Thrift.MessageType.REPLY, seqid);
      } else {
        result_obj = new Thrift.TApplicationException(Thrift.TApplicationExceptionType.UNKNOWN, err.message);
        output.writeMessageBegin("endServiceDelivery", Thrift.MessageType.EXCEPTION, seqid);
      }
      result_obj.write(output);
      output.writeMessageEnd();
      output.flush();
    });
  }
};
